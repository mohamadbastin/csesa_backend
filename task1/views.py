from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from task1.serializers import *
from .bot_utils import bot

from .data import ls


# Create your views here.


class GetTelegramData(CreateAPIView):
    serializer_class = TelegramSerializer

    def post(self, request, *args, **kwargs):
        # a = request.data.get('pwd')
        # if a == "mmdjun":
        # make()
        # print(ls)
        # message_poll_start_thread()
        for i in ls:
            try:
                TelegramUser.objects.get(telegram_id=i['id'])
            except TelegramUser.DoesNotExist:
                TelegramUser.objects.create(name=i['name'], username=i['username'], telegram_id=i['id'])
        return Response({"done": "done"})


class TelegramListView(ListAPIView):
    serializer_class = TelegramSerializer
    # TelegramUser.objects.all().delete()
    queryset = TelegramUser.objects.all()


class GetData(ListAPIView):
    serializer_class = ParticipantSerializer

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'msg': "good. you're here. \nin order to register you need to send me your telegram "
                       "username in a json field.\nlike this: {'username': 'mohamad'} \n"
                       "you should POST this json to this url: 'https://task1.mbastin.ir/signup'\n"
                       "good luck."}, status=status.HTTP_200_OK)


class Participate(CreateAPIView):
    serializer_class = ParticipantSerializer

    def post(self, request, *args, **kwargs):
        a = request.data.get('username', None)

        if not a:
            return Response({'msg': 'no username'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            b = TelegramUser.objects.get(username=a)
            Participant.objects.create(telegram_user=b)
            # make
            bot.sendMessage(-1001301297404, '@' + b.username + ' completed the task!')
            return Response({'msg': 'well done!'}, status=status.HTTP_200_OK)
        except TelegramUser.DoesNotExist:
            return Response(
                {'msg': 'oh it seems like youre not in the CSESA BACKEND group...\n contact @mohamadbastin'},
                status=status.HTTP_404_NOT_FOUND)
