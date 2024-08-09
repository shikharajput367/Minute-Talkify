import vertexai
from vertexai.language_models import TextGenerationModel

#prompt="Chairman Wormsley (at the proper time and place, after taking the chair and striking the gavel on the table): This meeting of the CTAS County Commission will come to order. Clerk please call the role. (Ensure that a majority of the members are present.)Chairman Wormsley: Each of you has received the agenda. I will entertain a motion that the agenda be approved.Commissioner Brown: So moved.Commissioner Hobbs: Seconded"


def predict(prompt):
    vertexai.init()
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.1
    }

    model = TextGenerationModel.from_pretrained("text-bison@002")
    response = model.predict(
        prompt,
        **parameters
    )
    #print(response.text)
    return response.text
    # print(f"Response from Model: {response.text}")

