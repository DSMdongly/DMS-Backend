webpackJsonp([2],{Zws9:function(t,e){},bqQt:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=function(){return n.e(8).then(n.bind(null,"2qqO"))},s=function(){return n.e(9).then(n.bind(null,"wtSN"))},o={name:"SurveyQuestion",props:{question:{type:Object}},computed:{component:function(){return this.question.is_objective?i:s}}},r={render:function(){var t=this,e=t.$createElement;return(t._self._c||e)(t.component,{tag:"div",staticClass:"question-wrapper",attrs:{question:t.question},on:{"update:question":function(e){return t.$emit("update:question",e)}}})},staticRenderFns:[]};var u={name:"SurveyDetailRight",components:{SurveyQuestion:n("VU/8")(o,r,!1,function(t){n("Zws9")},"data-v-7610f49c",null).exports},data:function(){return{questions:[]}},props:{},methods:{load:function(){var t=this;this.$http.get("/survey/question",{headers:{Authorization:"JWT "+this.$cookie.getCookie("JWT")},params:{survey_id:this.$route.params.id}}).then(function(e){200===e.status?t.questions=e.data:204===e.status&&alert("존재하지 않는 설문조사입니다.")}).catch(function(t){console.log(t)})},submit:function(){var t=this,e=[];this.questions.forEach(function(n){var i=new FormData;i.append("question_id",n.id),i.append("answer",n.answer);var s=t.$http.post("/survey/question",i,{headers:{Authorization:"JWT "+t.$cookie.getCookie("JWT")}});e.push(s)}),this.$http.all(e).then(function(t){var e=t.filter(function(t){return 201===t.status});t.length===e.length?alert("설문조사 제출에 성공하였습니다."):alert("설문조사 제출에 실패하였습니다.")}).catch(function(){alert("설문조사 제출에 실패하였습니다.")})}},beforeMount:function(){this.load()}},a={render:function(){var t=this.$createElement,e=this._self._c||t;return e("div",{attrs:{id:"survey-detail-right-wrapper"}},[e("div",{attrs:{id:"survey-form-wrapper"}},[this._l(this.questions,function(t){return e("survey-question",{key:t.id,attrs:{question:t},on:{"update:question":function(e){t=e}}})}),this._v(" "),e("div",{attrs:{id:"airplane-button"},on:{click:this.submit}})],2)])},staticRenderFns:[]};var c=n("VU/8")(u,a,!1,function(t){n("vvPx")},"data-v-b5e477c2",null);e.default=c.exports},vvPx:function(t,e){}});
//# sourceMappingURL=2.77a4a90e5270f87811a2.js.map