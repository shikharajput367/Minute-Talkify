from langchain.prompts import PromptTemplate

def talking_prompt(context,user_input):

    format_template=""
    #for i in user_input:
    format_template += f"[{user_input}?]"

    context_template=f""" Instruction: Provide answer to
this question- {format_template}  
based on sentiment and prediction analysis from the below context conversation in bullet points .Also, if needed we can Utilize factors such as engagement level, purchase intent signals, past behavior, decision-making factors, and contextual analysis to provide a statistically sound prediction.
if relevent information is not present say 'Not present in given context'
    [CONTEXT]
    {context}
    [CONTEXT END]
    """
    
    
    

    PromptTemplate(template=context_template,input_variables=['context']).format(context=context)
    #print(context_template)
    return context_template
#minutes_prompt(context,format_components)