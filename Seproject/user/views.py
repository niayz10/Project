from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers import UserSerializer, SkillSerializer
from user.models import User, Skill


@api_view(['GET', 'POST'])
def list_of_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


    elif request.method == 'PUT':

        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response({'error': serializer.errors})


    elif request.method == 'DELETE':

        user.delete()

        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def list_of_skills(request):
    if request.method == 'GET':
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def skill_detail(request, skill_id):
    try:
        skill = Skill.objects.get(id=skill_id)
    except User.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)


    elif request.method == 'PUT':

        serializer = SkillSerializer(instance=skill, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response({'error': serializer.errors})


    elif request.method == 'DELETE':

        skill.delete()

        return Response({'deleted': True})


@api_view(['GET'])
def users_by_skill(request, skill_id):
    try:
        users = User.objects.filter(skill=Skill.objects.get(id=skill_id))
    except Skill.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == "GET":
        serializer = UserSerializer(data=users, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def user_by_status(request, st_id):
    users = User.objects.all()
    users_by_status = []
    for x in users:
        if x.status == st_id:
            users_by_status.append(x)

    serializer = UserSerializer(data=users_by_status, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def user_top(request):
    users = User.objects.all().order_by('-rait')
    serializer = UserSerializer(data=users, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data[0:10])


@api_view(['GET'])
def skill_top(request):
    skills = Skill.objects.all().order_by('-raiting')
    serializer = SkillSerializer(data=skills, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data[0:10])


@api_view(['GET'])
def skill_for_st(request, st_id):
    skills = Skill.objects.filter(status=st_id)
    serializer = SkillSerializer(data=skills, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


