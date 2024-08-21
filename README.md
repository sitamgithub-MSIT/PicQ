# PicQ

Visual Question Answering is the task of answering open-ended questions based on an image. They output natural language responses to natural language questions about the content of an image. This project uses one of the popular multimodal models, [MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6) from the Hugging Face model hub for visual question answering.

[MiniCPM-V-2_6](https://huggingface.co/openbmb/MiniCPM-V-2_6) is the latest model in the MiniCPM-V series, built on SigLip-400M and Qwen2-7B with 8B parameters. It introduces new features for multi-image and video understanding. It also supports multilingual capabilities and produces fewer tokens than most models, improving inference speed, first-token latency, memory usage, and power consumption. It is easy to use in various ways, including CPU inference, quantized models, and online demos.

## Project Structure

The project is structured as follows:

- `src`: The folder that contains the source code for the project.

  - `app` : The folder that contains the source code for main functionality of the application.

    - `model.py`: The file that contains the code for loading the model and the tokenizer.
    - `response.py`: The file that contains the function for generating the response for the input image and question.

  - `config.py`: This file contains the configuration for the used model.
  - `logger.py`: This file contains the logging configuration for the project.
  - `exception.py`: This file contains the exception handling for the project.

- `app.py`: The main file that contains the Gradio application for visual question answering.
- `model.py`: The file that contains the visual question-answering model.
- `requirements.txt`: The file that contains the required dependencies for the project.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder that contains the screenshots for working on the application.
- `images`: The folder that contains the images for testing the application.

## Tech Stack

- Python (for the programming language)
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

Now, open up your local host and you should see the web application running. If you would like more information, please refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/PicQ).

## Usage

The web application allows you to input an image and a question. The model will then generate an answer based on the image and the question. It can assist visually impaired individuals by providing access to web and real-world images, improving image retrieval by retrieving specific characteristics, and enabling video search by retrieving specific snippets or timestamps based on search queries. The application can also be applied in educational settings to provide a more interactive learning experience.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
