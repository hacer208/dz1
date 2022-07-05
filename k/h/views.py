from django.shortcuts import render
from django.http import HttpResponse


def index (requests):
    return HttpResponse("<h4>Привет Vlad, ты классный, больше не кричи на меня</h4>")


def about (requests):
    return HttpResponse("<h4>abaut</h4>")