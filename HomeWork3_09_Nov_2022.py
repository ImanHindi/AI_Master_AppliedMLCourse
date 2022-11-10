import re
import string


class text_edit():
    def __init__(self,input_f,output_f):
        self.input_f=input_f
        self.output_f=output_f

    def get_report(self,edited_text):
        report=dict()
        #no_of_words=len(list(edited_text.lower().strip().split(" ")))
        text=edited_text.translate(str.maketrans('', '', string.punctuation)).lower().strip()
        report['no of words']=len(text.split(" "))
        report['words']=set(text.split(" "))
        report['no of unique words']=len(report['words'])
        report['word frequency']={keyword:str(text.count(keyword)) for keyword in report['words']}
        return report
    def edit_and_save_file(self):
        with open(self.input_f, 'r') as f:
            text = f.read()
        out_string = re.sub(r"\n+", " ", text).strip()
        res = re.sub(' +', ' ', out_string)
        print("res", res)
        with open(self.output_f, 'w') as f:
            f.write(res)
        return res

input_file=input("please insert input file path")
output_file=input("please insert output file name")
new_text=text_edit(input_file,output_file)
edited_text=new_text.edit_and_save_file()
report=new_text.get_report(edited_text)
for key,value in report.items():
    print(f"{key}:\n{value}\n")