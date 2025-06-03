"""THINGS NEED TO DO IN ORDER TO RUN THIS"""
#install python in extension
#install env in extension
#pip install google-generativeai
#pip install python-dotenv

import tkinter as tk
from tkinter import messagebox
import os
import google.generativeai as genai

class FLAMESCHAT:
    def __init__(self):
        self.history = []
        self.API_Config()
        
        self.flames = tk.Tk()
        self.flames.title("PHINMA University of Pangasinan")
        self.flames.geometry("800x750")
        
        FlamesChatLogo = tk.PhotoImage(file="FlamesChat Logo.png")
        self.flames.iconphoto(False, FlamesChatLogo)
        self.flames.config(background="khaki")
        
        self.Logo = FlamesChatLogo.subsample(5,5)

        self.setup_header()
        self.setup_faq_section()
        self.setup_chat_section()
        
        self.flames.mainloop()

    def API_Config(self):
        os.environ["GEMINI_API_KEY"] = "AIzaSyDIpa9bmcKBFf8QtwPq-a7-kS3RkyhCktU"
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

    def setup_header(self):
        header_frame = tk.Frame(self.flames, bg="black", highlightbackground="#cc8c05", highlightthickness=5)
        header_frame.pack(pady=20)
        
        logo_label = tk.Label(header_frame, image=self.Logo, justify="left", highlightbackground="#cc8c05", highlightthickness=.5, bg= "#cc8c05")
        logo_label.pack(side=tk.LEFT)
        
        title_label = tk.Label(header_frame, text="FLAMESCHATBOT", font=("Arial", 24, "bold"), fg="gold", bg="black")
        title_label.pack(side=tk.LEFT, padx=20)
        
        canvas = tk.Canvas(self.flames, width=800, height=5, bg="#cc8c05", highlightthickness=0)
        canvas.pack(pady=10)
        canvas.create_line(0, 2, 800, 2, fill="#cc8c05", width=3)

    def setup_faq_section(self):
        self.faqs = {
            "What is PHINMA University of Pangasinan?" : "The PHINMA – University of Pangasinan, also known as UPang, is a private and non-sectarian university located at Dagupan, Pangasinan, Philippines. It is a member of the PHINMA Education Network (PEN). It offers practically all undergraduate and graduate courses that Metro Manila universities offer.",
            "When did University of Pangasinan become a member of PHINMA?": "In 2009, the University of Pangasinan became a member of the PHINMA Education Network (PEN), an educational institution that aims to provide quality education at an affordable fee.",
            "What is the hymm of PHINMA University of Pangasinan?": "\"UPANG Hymn LYRICS\"\n\nAll hail you UPang\nWe stand tall and proud\nOf your glorious legacy\nWe sing out loud\n\nPatria Virtus Scientia\nWe say these words with pride\nLet our noble vision\nLight up our lives\n\nAlma Mater dear\nIn your warm embrace\nWe wave your banner high\nMay your torch forever blaze\n\nAll hail you UPang\nTo heaven we implore\nThat you be blessed, oh UPang\nForevermore\nAlma Mater dear\nIn your warm embrace\nWe wave your banner high\nMay your torch forever blaze\n\nAll hail you UPang\nTo heaven we implore\nThat you be blessed, oh UPang\nForevermore\n\nMay you be blessed, oh UPang\nForevermore",
            "Where is the PHINMA University of Pangasinan known?": "PHINMA UPang is known for having a high employment rate with 81% of newly graduate students having secured a job within the year after their graduation. UPang is also known as one of the top performing school in the Philippines especially in the field of Medical Courses",
            "What are the core values of PHINMA University Pangasinan?": "PHINMA University of Pangasinan Core Values\n•Integrity.\n•Competence.\n•Commitment.\n•Professionalism.\n•Teamwork.\n•Openness.",
            "What is Hawak Kamay Scholarship?" : "The Hawak Kamay Scholarship is a financial assistance program designed to support deserving Filipino students, particularly from low-income families, in their educational pursuits.",
            "What courses are offered at the University of Pangasinan?" : "UPang offers a wide range of undergraduate and graduate programs in various fields, including business administration, nursing, information technology, education, engineering, and law",
            "What are the admission requirements of the University of Pangasinan?" : "The admission requirements for UPang include a PSA birth certificate, high school/senior high school report card (Form 138), and Form 137. For Hawak Kamay (HK) scholars, an HK certificate is also required",
            "Contact of PHINMA University of Pangasinan" : "Mobile No: +63 995-078-5660\nTelephone No: (075) 522-5635\nEmail: info.up@phinmaed.com"
        }

        faq_label = tk.Label(self.flames, text="FREQUENTLY ASK QUESTIONS", font=("Arial", 12, "bold"), fg="white", bg="black", highlightbackground="#cc8c05", highlightthickness=3)
        faq_label.pack(pady=10)
        
        click_label = tk.Label(self.flames, text="Click the questions below", font=("Arial", 9), fg="white", bg="black", highlightbackground="#cc8c05", highlightthickness=3)
        click_label.pack(pady=10)

        self.faq_listbox = tk.Listbox(self.flames, width=60, height=10, font=("Arial", 12,), fg="yellow", bg="black", justify="center", highlightbackground="#cc8c05", highlightthickness=3)
        self.faq_listbox.pack(pady=5)

        for question in self.faqs.keys():
            self.faq_listbox.insert(tk.END, question)

        self.faq_listbox.bind("<<ListboxSelect>>", self.show_answer_from_list)

    def setup_chat_section(self):
        question_label = tk.Label(self.flames, text="FLAMES CHATBOT AI", font=("Arial", 12, "bold"), fg="white", justify="center", bg="black", highlightbackground="#cc8c05", highlightthickness=3)
        question_label.pack(pady=10)
        
        enter_label = tk.Label(self.flames, text="Enter your inquiries below", font=("Arial", 9), fg="white", justify="center", bg="black", highlightbackground="#cc8c05", highlightthickness=3)
        enter_label.pack(pady=10)

        self.question_entry = tk.Entry(self.flames, width=50, font=("Arial", 12), highlightbackground="#cc8c05", highlightthickness=3)
        self.question_entry.pack(pady=10)

        EnterButton = tk.Button(self.flames, text="Enter", command=self.UserQuestion, font=("Arial", 12), fg="white", bg="green", width=5, height=1)
        EnterButton.pack(pady=20)

    def UserQuestion(self):
        question = self.question_entry.get().strip()
        answer = self.faqs.get(question.capitalize())

        if answer:
            messagebox.showinfo("Answer", answer)
        else:
            try:
                chat_session = self.model.start_chat(history=self.history)
                response = chat_session.send_message(question)
                model_response = response.text
                messagebox.showinfo("FLAMESCHATBOT", model_response)

                self.history.append({"role": "user", "parts": [question]})
                self.history.append({"role": "model", "parts": [model_response]})
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        self.question_entry.delete(0, tk.END)

    def show_answer_from_list(self, event):
        selected_question = self.faq_listbox.get(self.faq_listbox.curselection())
        answer = self.faqs.get(selected_question)
        if answer:
            messagebox.showinfo("Answer", answer)

if __name__ == "__main__":
    FLAMESCHAT()
