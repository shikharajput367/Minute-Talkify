from langchain.prompts import PromptTemplate

#context='C:\\Users\\ajain2\\Downloads\\minutes_generator\\minutes_generator\\customer_conversation.txt'
def minutes_prompt(context):
    template = """If in below format likelihood or BPS is asked then Analyze the conversation to predict the likelihood of the customer making a purchase on a scale from 1 to 100 and Factors Contributing to Prediction. 
     If in below format Strategies to Improve Probability of Sale is asked then  Utilize factors such as engagement level, purchase intent signals, past behavior, decision-making factors, and contextual analysis to provide a statistically sound prediction.
      If in below format Strategies to Improve Probability of Sale is asked then  suggest strategies to improve the probability of making a sale and provide talking points to effectively engage the customer.
     If in below format common questions is asked then provide common questions asked by customers during the conversation and compile a list for future follow-up. 
     Include these frequently asked questions in marketing strategies to address potential concerns and improve sales. 
     Suggestions and follow-up questions should be based on comprehensive analysis and data-driven insights.
     Provide answers in details based on the format provided below and don't give additional information that is not asked in the format
     Also, provide more additional details based on sentiment and predictive analysis
    [CONTEXT]
    {context}
    [CONTEXT END]
    [FORMAT]
        DATE:
        ATTENDEES:
        Important Key Points:
        Future Plans: 
    [FORMAT END]
    """
    formatted_template = PromptTemplate(template=template,input_variables=['context']).format(context=context)
    print(formatted_template)

minutes_prompt(context)