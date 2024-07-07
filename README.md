# SalesTrek AI Coach

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/SalesTrek-AI-Coach/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-0.88.0-green)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/langchain-google--gemini--pro-green)](https://langchain.com/)
[![Google Gemini Pro](https://img.shields.io/badge/google--gemini--pro-API-red)](https://cloud.google.com/ai/gemini)

SalesTrek AI Coach is an intelligent, AI-driven sales assistant designed to help sales teams enhance their performance. It provides support for generating cold call scripts, crafting effective email templates, handling objections, and more. The application is built using Python and Streamlit, with AI functionalities powered by Google's Gemini Pro model and LangChain.

## Features

- **Cold Call Script Generation**: Create effective cold call scripts tailored to your company's products and services.
- **Email Template Crafting**: Generate engaging email templates for various sales scenarios.
- **Objection Handling Advice**: Get expert tips on addressing common objections in your industry.
- **Sales Tips and Strategies**: Receive advice on closing deals, prospecting, lead generation, and more.
- **Sales Management Guidance**: Tips for managing and leading a sales team, tracking performance, and forecasting sales.
- **Customizable**: Incorporate your company's unique context and values into the AI's responses.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/SalesTrek-AI-Coach.git
    cd SalesTrek-AI-Coach
    ```

2. **Set Up Environment**:
    - Create and activate a virtual environment (optional but recommended):
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```
    - Install the required packages:
      ```bash
      pip install -r requirements.txt
      ```

3. **Configure Environment Variables**:
    - Create a `.env` file in the root directory of the project.
    - Add your Google API key to the `.env` file:
      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Access the Application**:
    - Open your web browser and navigate to `http://localhost:8501` to access the SalesTrek AI Coach interface.

2. **Interacting with the AI Coach**:
    - Use the input box to type your requests. You can ask for help with generating scripts, handling objections, crafting emails, and more.
    - Use specific commands to call different functionalities:
        - `/script [your request]`: Generate a sales script.
        - `/email [your request]`: Generate an email template.
        - General questions or requests will be handled by the AI sales coach.

## Customization

- **Styling**:
    - Custom CSS is used to style the application. The CSS file is located at `styles.css`. Modify this file to change the look and feel of the application.

- **Expanding Functionalities**:
    - To add new functionalities or modify existing ones, edit the functions in the `gen.py` module.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Powered by [Google Gemini Pro](https://cloud.google.com/ai/gemini) and [LangChain](https://langchain.com/).
- Built with [Streamlit](https://streamlit.io/).

