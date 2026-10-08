import requests
import streamlit as st
import PyPDF2

st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🤖",
    layout="centered"
)

st.title("AI Career Coach")
st.write("Upload your CV and enter the target role.")


# API settings
API_URL = "https://economic-smith-gurgling.ngrok-free.dev/generate"
BEARER_TOKEN = "nothing111"


with st.form("generate_form"):

    # Upload CV
    uploaded_cv = st.file_uploader(
        "Upload your CV",
        type=["pdf"],
    )

    # Target role
    target_role = st.text_input(
        "Target Role",
        placeholder="e.g. RTL Design Engineer"
    )

    submitted = st.form_submit_button(
        "Extract CV data",
        type="primary"
    )


if submitted:

    # Validate CV
    if uploaded_cv is None:
        st.error("Please upload your CV PDF.")

    # Validate target role
    elif not target_role.strip():
        st.error("Please enter the target role.")

    else:

        # ---------------------------------------------------------
        # Extract text from PDF
        # ---------------------------------------------------------

        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_cv)

            pages_text = []

            for page in pdf_reader.pages:
                page_text = page.extract_text()

                if page_text:
                    pages_text.append(page_text)

            full_text = "\n".join(pages_text)

        except Exception as exc:
            st.error(f"Could not read the PDF: {exc}")
            full_text = ""

        # Check that text was actually extracted
        if not full_text.strip():
            st.error(
                "Could not extract text from the PDF. "
                "The PDF may contain scanned images instead of selectable text."
            )

        else:

            # ---------------------------------------------------------
            # Prepare API request
            # ---------------------------------------------------------

            headers = {
                "Authorization": f"Bearer {BEARER_TOKEN}"
            }

            payload = {
                "full_text": full_text,
                "target_role": target_role.strip()
            }

            # ---------------------------------------------------------
            # Send request to FastAPI
            # ---------------------------------------------------------

            with st.spinner("Contacting the API…"):

                try:

                    response = requests.post(
                        API_URL,
                        headers=headers,
                        json=payload,
                        timeout=300
                    )

                except requests.RequestException as exc:

                    st.error(f"Could not reach the API: {exc}")

                else:

                    # -------------------------------------------------
                    # Parse API response
                    # -------------------------------------------------

                    try:
                        result = response.json()

                    except ValueError:

                        result = {
                            "detail": response.text
                            or "The API returned no JSON."
                        }

                    # -------------------------------------------------
                    # Successful response
                    # -------------------------------------------------

                    if response.ok:

                        st.success(
                            "CV data extracted successfully."
                        )

                        st.subheader("Target Role")
                        st.write(target_role)

                        st.subheader("Extracted data")

                        extracted = result.get(
                            "response",
                            result
                        )

                        if isinstance(extracted, (dict, list)):
                            st.json(extracted)

                        else:
                            st.write(extracted)

                    # -------------------------------------------------
                    # Failed response
                    # -------------------------------------------------

                    else:

                        st.error(
                            f"Request failed "
                            f"(HTTP {response.status_code})."
                        )

                        detail = (
                            result.get("detail", result)
                            if isinstance(result, dict)
                            else result
                        )

                        if isinstance(detail, str) and (
                            "OUTPUT_PARSING_FAILURE" in detail
                            or "invalid JSON object" in detail
                        ):

                            st.warning(
                                "The API received the request, but "
                                "the CV extraction model returned "
                                "text that could not be parsed as JSON."
                            )

                            st.code(detail)

                        elif isinstance(detail, (dict, list)):

                            st.json(detail)

                        else:

                            st.code(str(detail))