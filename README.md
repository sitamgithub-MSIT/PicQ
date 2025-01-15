# PicQ

Visual Question Answering is answering open-ended questions based on an image. They output natural language responses to natural language questions about the content of an image. This project uses one of the popular multimodal models, [**MiniCPM-o 2.6**](https://huggingface.co/openbmb/MiniCPM-o-2_6) from the Hugging Face model hub.

[**MiniCPM-o 2.6**](https://huggingface.co/openbmb/MiniCPM-o-2_6) is the latest and most capable model in the MiniCPM-o series, built on **SigLip-400M**, **Whisper-medium-300M**, **ChatTTS-200M**, and **Qwen2.5-7B** with a total of 8B parameters. MiniCPM-o 2.6 significantly improves upon its predecessor, boasting advanced real-time speech conversation and multimodal live streaming capabilities. It surpasses proprietary models in visual and speech understanding, offers efficient processing, and provides easy usage options.

## Project Structure

The project is structured as follows:

- `src\`: The folder containing the project's source code.

  - `minicpm\`: The folder containing the source code for the application's main functionality.

    - `model.py`: The file that contains the code for loading the model, tokenizer, and processor.
    - `response.py`: The file that contains the function for generating the response for the input image and question.

  - `config.py`: This file contains the configuration for the used model.
  - `logger.py`: This file contains the project's logging configuration.
  - `exception.py`: This file contains the exception handling for the project.

- `app.py`: The main file that contains the Gradio application for visual question answering.
- `requirements.txt`: The file containing the project's required dependencies.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder containing screenshots for working on the application.
- `images`: The folder that contains the images for testing the application.

## Tech Stack

- Python (for the programming language)
- PyTorch (for the deep learning framework)
- Hugging Face Transformers Library (for the visual question-answering model)
- Gradio (for the web application)
- Hugging Face Spaces (for hosting the gradio application)

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/PicQ.git`
2. Change the directory: `cd PicQ`
3. Create a virtual environment: `python -m venv tutorial-env`
4. Activate the virtual environment: `tutorial-env\Scripts\activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the Gradio application: `python app.py`

Now, open up your local host and see the web application running. For more information, please refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/PicQ).

**Note**: You need a Hugging Face access token to run the application. You can get the token by signing up on the Hugging Face website and creating a new token from the settings page. After getting the token, you can set it as an environment variable `ACCESS_TOKEN` in your system by creating a `.env` file in the project's root directory. Check the `.env.example` file for reference.

The application is hosted on Hugging Face Spaces running on a GPU. You are expected to have a GPU for local use when running the application. If you do not have a GPU, you can explore the local inference option provided by the model [here](https://github.com/OpenBMB/llama.cpp/blob/minicpm-omni/examples/llava/README-minicpmo2.6.md).

## Usage

The web application allows you to input an image and a question. The model will then generate an answer based on the image and the question. It can assist visually impaired individuals by providing access to web and real-world images, improving image retrieval by retrieving specific characteristics, and enabling video search by retrieving specific snippets or timestamps based on search queries. The application can also be applied in educational settings to provide a more interactive learning experience.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
