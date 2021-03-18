from transformers import pipeline
import torch
# using pipeline API for summarization task
class aiReadingModels():
    def __init__(self):
        device_a=torch.cuda.is_available()
        if device_a:
            self.device="cuda:0"
        else:
            self.device="cpu"
    def summaryGeneration(self,textToSummarize):
        summaryModel=pipeline("summarization",device=0)
        summary_text=summaryModel(textToSummarize)[0]['summary_text']
        return summary_text
    def qaModelGeneration(self,question,context):
        qaModel=pipeline('question-answering',device=0)
        outputs=qaModel(question=question,context=context)
        return (outputs['answer'],outputs['score'])
    def textGen(self,startText,max_length=200,num_return_sequences=3):
        generate=pipeline("text-generation",model="gpt2")
        outputs=generate(startText,max_length=max_length,num_return_sequences=num_return_sequences)
        return outputs

