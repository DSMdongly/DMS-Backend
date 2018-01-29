import json

from flask import Blueprint, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Api, abort, request
from flasgger import swag_from

from app.docs.admin.survey.survey import *
from app.models.account import AdminModel
from app.models.survey import QuestionModel, SurveyModel
from app.views import BaseResource

api = Api(Blueprint('admin-survey-api', __name__))
api.prefix = '/admin'


@api.resource('/survey')
class SurveyManaging(BaseResource):
    @swag_from(SURVEY_MANAGING_GET)
    @jwt_required
    def get(self):
        """
        설문지 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        response = [{
            'id': str(survey.id),
            'creation_time': str(survey.creation_time)[:10],
            'title': survey.title,
            'description': survey.description,
            'start_date': str(survey.start_date),
            'end_date': str(survey.end_date)
        } for survey in SurveyModel.objects if len(survey.questions)]

        return self.json_response(response)

    @swag_from(SURVEY_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        설문지 등록
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

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
            target=target
        ).save()

        return {
            'id': str(survey.id)
        }, 201

    @swag_from(SURVEY_MANAGING_DELETE)
    @jwt_required
    def delete(self):
        """
        설문지 제거
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

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
    @swag_from(QUESTION_MANAGING_GET)
    @jwt_required
    def get(self):
        """
        설문지의 질문 리스트 조회
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

        survey_id = request.args['survey_id']
        if len(survey_id) != 24:
            return Response('', 204)

        survey = SurveyModel.objects(id=survey_id).first()
        if not survey:
            return Response('', 204)

        response = [{
            'id': str(question.id),
            'title': question.title,
            'is_objective': question.is_objective,
            'choice_paper': question.choice_paper if question.is_objective else None
        } for question in survey.questions]

        return self.json_response(response)

    @swag_from(QUESTION_MANAGING_POST)
    @jwt_required
    def post(self):
        """
        설문지에 질문 등록
        """
        admin = AdminModel.objects(id=get_jwt_identity()).first()
        if not admin:
            abort(403)

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

            survey.questions.append(QuestionModel(
                title=title,
                is_objective=is_objective,
                choice_paper=question['choice_paper'] if is_objective else []
            ))

        return Response('', 201)
