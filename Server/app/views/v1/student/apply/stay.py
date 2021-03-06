from datetime import datetime, time

from flask import Blueprint, Response, current_app, g, request
from flask_restful import Api


from app.views.v1 import BaseResource
from app.views.v1 import student_only


from app.models.apply import StayApplyModel

api = Api(Blueprint('student-stay-api', __name__))


@api.resource('/stay')
class Stay(BaseResource):

    @student_only
    def get(self):
        """
        잔류신청 정보 조회
        """
        student = g.user

        apply = StayApplyModel.objects(student=student).first()

        return self.unicode_safe_json_response({
            'value': apply.value
        }, 200)


    @student_only
    def post(self):
        """
        잔류신청
        """
        student = g.user

        now = datetime.now()

        if current_app.testing or (now.weekday() == 6 and now.time() > time(20, 30)) or (0 <= now.weekday() < 3) or (now.weekday() == 3 and now.time() < time(22, 00)):
            # 신청 가능 범위
            # - 일요일 오후 8시 30분 이후부터 목요일 오후 10시까지
            # weekday는 월요일이 0, 일요일이 6
            value = int(request.form['value'])

            StayApplyModel.objects(student=student).delete()
            StayApplyModel(student=student, value=value, apply_date=datetime.now()).save()

            return Response('', 201)
        else:
            return Response('', 204)
