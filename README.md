# PicQ

Visual Question Answering is the task of answering open-ended questions based on an image. They output natural language responses to natural language questions about the content of an image. This project uses one of the popular multimodal models, [MiniCPM-Llama3-V-2_5](https://huggingface.co/openbmb/MiniCPM-Llama3-V-2_5) from the Hugging Face model hub for visual question answering. The used model can be run only on GPUs (A100).

## Tech Stack

- Python (for the programming language)
- Hugging Face Transformers Library (for the visual question answering model)
- Gradio (for the web application)
- Hugging Face Spaces (for hosting the gradio application)

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/PicQ.git`
2. Create a virtual environment: `python -m venv tutorial-env`
3. Activate the virtual environment: `tutorial-env\Scripts\activate`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Run the Gradio application: `python app.py`

Now, open up your local host and you should see the web application running. For more information, refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/PicQ).

## Usage

The web application allows you to input an image and a question. The model will then generate an answer based on the image and the question. It can assist visually impaired individuals by providing access to web and real-world images, improving image retrieval by retrieving specific characteristics, and enabling video search by retrieving specific snippets or timestamps based on search queries. The application can also be applied in educational settings to provide a more interactive learning experience.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
