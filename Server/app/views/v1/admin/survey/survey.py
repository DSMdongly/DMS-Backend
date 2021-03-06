from datetime import datetime
import json

from flask import Blueprint, Response, request
from flask_restful import Api


from app.views.v1 import BaseResource
from app.views.v1 import admin_only


from app.models.survey import QuestionModel, SurveyModel
from app.models.support.mongo_helper import mongo_to_dict

api = Api(Blueprint('admin-survey-api', __name__))
api.prefix = '/admin'


@api.resource('/survey')
class SurveyManaging(BaseResource):

    @admin_only
    def get(self):
        """
        설문지 리스트 조회
        """
        response = [mongo_to_dict(survey, ['target']) for survey in SurveyModel.objects]

        return self.unicode_safe_json_response(response)


    @admin_only
    def post(self):
        """
        설문지 등록
        """
        title = request.form['title']
        description = request.form['description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        target = json.loads(request.form['target'])

        survey = SurveyModel(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            target=target,
            creation_time=datetime.now()
        ).save()

        return self.unicode_safe_json_response({
            'id': str(survey.id)
        }, 201)


    @admin_only
    def delete(self):
        """
        설문지 제거
        """
        survey_id = request.form['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        survey.delete()

        return Response('', 200)


@api.resource('/survey/question')
class QuestionManaging(BaseResource):

    @admin_only
    def get(self):
        """
        설문지의 질문 리스트 조회
        """
        survey_id = request.args['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        response = [mongo_to_dict(question, ['survey']) for question in QuestionModel.objects(survey=survey)]

        return self.unicode_safe_json_response(response)


    @admin_only
    def post(self):
        """
        설문지에 질문 등록
        """
        rq = request.json

        survey_id = rq['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        questions = rq['questions']
        for question in questions:
            title = question['title']
            is_objective = question['is_objective']

            QuestionModel(
                survey=survey,
                title=title,
                is_objective=is_objective,
                choice_paper=question['choice_paper'] if is_objective else []
            ).save()

        return Response('', 201)
