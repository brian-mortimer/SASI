import os
from datetime import datetime
import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever, FARMReader, PreProcessor
from haystack.pipelines import ExtractiveQAPipeline
from haystack.utils import convert_files_to_docs


CONFIDENCE_THRESHOLD_UPPER = 0.7
CONFIDENCE_THRESHOLD_LOWER = 0.05

logging.basicConfig(
    format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
logging.getLogger("haystack").setLevel(logging.INFO)

# initializes document stores for each category of question
document_store_location_questions = InMemoryDocumentStore(use_bm25=True)
document_store_course_codes_questions = InMemoryDocumentStore(use_bm25=True)
document_store_Modules_codes_questions = InMemoryDocumentStore(use_bm25=True)
document_store_Timetables_questions = InMemoryDocumentStore(use_bm25=True)


# test file directory
doc_dir = os.path.join(os.getcwd(), "data/test_data")

processor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=True,
    remove_substrings=None,
    split_by="passage",
    split_length=200,
    split_respect_sentence_boundary=False,
    split_overlap=0
)

# Catagories data
categories = {
    'locations': document_store_location_questions,
    'course_codes': document_store_course_codes_questions,
    'Modules': document_store_Modules_codes_questions,
    'Timetables': document_store_Timetables_questions,
    # ... more categories as needed
}

# converts test files to documents and stores in separate document stores
for category, document_store in categories.items():
    category_dir = os.path.join(doc_dir, category)
    all_docs = convert_files_to_docs(
        dir_path=category_dir, split_paragraphs=True)
    docs = processor.process(all_docs)
    document_store.write_documents(docs)

# initializes retrievers
retriever_location_questions = BM25Retriever(
    document_store=document_store_location_questions)
retriever_course_codes_questions = BM25Retriever(
    document_store=document_store_course_codes_questions)
retriever_Modules_codes_questions = BM25Retriever(
    document_store=document_store_Modules_codes_questions)
retriever_Timetables_questions = BM25Retriever(
    document_store=document_store_Timetables_questions)
# ... more retrievers as needed

# initializes reader
reader = FARMReader(
    model_name_or_path="deepset/roberta-base-squad2", use_gpu=False)


# create retriever-reader pipelines
pipe_location_questions = ExtractiveQAPipeline(
    reader, retriever_location_questions)
pipe_course_code_questions = ExtractiveQAPipeline(
    reader, retriever_course_codes_questions)
pipe_Modules_codes_questions = ExtractiveQAPipeline(
    reader, retriever_Modules_codes_questions)
pipe_Timetables_questions = ExtractiveQAPipeline(
    reader, retriever_Timetables_questions)
# ... more pipelines as needed


class ActionHaystackModuleCodes(Action):
    """
    Haystack Action for Module Codes.
    """

    def __init__(self):
        self.pipe = pipe_Modules_codes_questions

    def name(self) -> Text:
        return "call_haystack_for_module_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:

        query = tracker.latest_message["text"]
        response = self.pipe.run(query=query)
        print(response["answers"][0].score)
        print(response["answers"][0].context)

        if response["answers"]:
            if response["answers"][0].score > CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer
            elif response["answers"][0].score > CONFIDENCE_THRESHOLD_LOWER and response["answers"][0].score < CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer + \
                    " *Note: This is a low confidence answer. Please consider rephrasing your question with more information"
            else:
                answer = "I am unable to process your request please vist www.ul.ie for more information"

        else:
            answer = "No Answer Found!"

        dispatcher.utter_message(text=answer)

        return []


class ActionHaystackRoomLocation(Action):
    """
    Haystack Action for Room Locations.
    """

    def __init__(self):
        self.pipe = pipe_location_questions

    def name(self) -> Text:
        return "call_haystack_for_room_location_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:

        query = tracker.latest_message["text"]
        response = self.pipe.run(query=query)
        print(response["answers"][0].score)
        print(response["answers"][0].context)

        if response["answers"]:
            if response["answers"][0].score > CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer
            elif response["answers"][0].score > CONFIDENCE_THRESHOLD_LOWER and response["answers"][0].score < CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer + \
                    " *Note: This is a low confidence answer. Please consider rephrasing your question with more information"
            else:
                answer = "I am unable to process your request please vist www.ul.ie for more information"

        else:
            answer = "No Answer Found!"

        dispatcher.utter_message(text=answer)

        return []


class ActionHaystackCourseCodes(Action):
    """
    Haystack Action for Course Codes.
    """

    def __init__(self):
        self.pipe = pipe_course_code_questions

    def name(self) -> Text:
        return "call_haystack_for_course_codes_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:

        query = tracker.latest_message["text"]
        response = self.pipe.run(query=query)
        print(response["answers"][0].score)
        print(response["answers"][0].context)

        if response["answers"]:
            if response["answers"][0].score > CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer
            elif response["answers"][0].score > CONFIDENCE_THRESHOLD_LOWER and response["answers"][0].score < CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer + \
                    " *Note: This is a low confidence answer. Please consider rephrasing your question with more information"
            else:
                answer = "I am unable to process your request please vist www.ul.ie for more information"

        else:
            answer = "No Answer Found!"

        dispatcher.utter_message(text=answer)

        return []


class CourseForm(Action):
    """
    Haystack Action for Course form.
    """

    def name(self) -> Text:
        return "validate_course_form"

    def __init__(self):
        self.pipe = pipe_Timetables_questions

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["courseName", "courseYear"]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:

        course_name = tracker.get_slot('courseName')
        course_year = tracker.get_slot('courseYear')

        if (course_name != None) & (course_year != None):
            query = nextLectureQuery()
            query.run(dispatcher, tracker, domain)

        return []


class nextLectureQuery():
    """
    Haystack Action for next lecture.
    """

    def name(self) -> Text:
        return "next_lecture_query"

    def __init__(self):
        self.pipe = pipe_Timetables_questions

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:

        course_name = tracker.get_slot('courseName')
        course_year = tracker.get_slot('courseYear')

        dtime = datetime.now()
        todays_day = dtime.strftime('%A')

        query = f"What is the timetable for [{course_name}](courseName) [{course_year}](courseYear) [{todays_day}](day)"
        response = self.pipe.run(query=query)

        if response["answers"]:
            answer = response["answers"][0].context
        else:
            answer = "No Answer Found!"

        dispatcher.utter_message(text=answer)


class ActionTimetableQuery(Action):
    """
    Haystack Action for Timetables.
    """

    def name(self) -> Text:
        return "timetable_query"

    def __init__(self):
        self.pipe = pipe_Timetables_questions

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:

        query = tracker.latest_message["text"]
        response = self.pipe.run(query=query)

        if response["answers"]:
            if response["answers"][0].score > CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer
            elif response["answers"][0].score > CONFIDENCE_THRESHOLD_LOWER and response["answers"][0].score < CONFIDENCE_THRESHOLD_UPPER:
                answer = response["answers"][0].answer + \
                    " *Note: This is a low confidence answer. Please consider rephrasing your question with more information"
            else:
                answer = "I am unable to process your request please vist www.ul.ie for more information"
        else:
            answer = "No Answer Found!"

        dispatcher.utter_message(text=answer)

        return []
