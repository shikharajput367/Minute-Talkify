# Minutes of Meeting Generator (MoM Generator)

### Code Directory Structure
- Scripts contains utility functions and other components can go there the file for now is:
    * `utils.py` : this module contains functions for reading and splitting the contents of the file
- `generator.py` : this module contains a predict function that calls the text bison model on vertex ai platform to generate the output
- `prompts.py` : one common place to store all prompts for different use cases for now it just contains one prompt that instructs the model on how to create the required output.
- `main.py` : this is the entry point which contains the following
    * A `streamlit` application that displays the transcript contents and subsequently the output
    * this file calls the utility functions defined in `utils` to transcript contents and split the contents into chunks
    * a call to the LLM to generate the output

### Python Dev Setup
NOTE: Make sure python is atleast 3.10 or 3.9 I have used 3.10

development using **python environments**

* After unzipping the open and navigating to the folder on the appropriate shell application
* create a python environment by either:
    * using conda : ```conda create -n <env_name> python=3.10```
    * using venv : ```python -m venv venv```
* based on how the environment was created make sure to activate the environment
    * for conda : ```conda activate <env_name>```
    * for venv windows: ```<env_name>\Scripts\activate```
    * for venv linux : ```source <env_name>/bin/activate```
* after the environment is activated run the command ```pip install -r requirements.txt```

development without using **python environments**

if for any reasons there is need to use the system installation of python for development make sure the version is atleast ***3.9*** and then follow the steps
* navigate to the project in the shell
* run the command : ```pip install -r requirements.txt```

### Google Auth
NOTE : Make sure to have google cloud cli installed on the machine and is set to path

test : run the `gcloud -v` command and if no output is displayed then install gcloud tool on the machine

* once we have gcloud we need to initialize a project configuration : `gcloud init` and follow the steps on the login step use your mastermind id and for project selection use the fsihackathon project

* after the above step run the command `gcloud auth application-default login` use your mastermind id to login if no errors come and we are able to set a **quota project** we have succesfully configured and connected to our google cloud project from the local dev machine

### running the code
* once the above steps are done run: `streamlit run main.py` to run the ui for the application in dev mode
* make sure you are in the project directory before running the above command

### misc
* for the moment the file getting read is `test.txt` which is present in the project if new transcripts are to be tested just overite the contents in `test.txt` and run the process on ui for looking at the minutes

* file upload functionality will be developed to remove the test.txt dependency.