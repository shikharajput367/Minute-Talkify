from langchain.prompts import PromptTemplate
#context='adffgb'
#format_components=['a','b','c']
def minutes_prompt(context,format_components):
    format_template=""
    format_template += "["
    for i in format_components:
        format_template += f"\t{i},"
    format_template += "]"

    context_template=f""" Instruction: Create a meeting summary strictly for only
{format_template}  from the below context  in dot bullet points 
if relevent information is not present say 'Info not present in transcipt'



    [CONTEXT]
    {context}
    [CONTEXT END]
    """
    
    
    

    #template = Instruction+ context_template 
    #formatted_template = PromptTemplate(template=context_template,input_variables=['context']).format(context=context)
    #print(context_template)
    return context_template
#minutes_prompt(context,format_components)