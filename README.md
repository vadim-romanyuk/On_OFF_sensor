{% extends 'interaction/base.html' %}

{% block title %} About {% endblock %}
{%  load static %}

{% block content %}
    <style>
   .text {
    text-align:  center;
   }
  </style>
   <h1 class="text" >Проект: ON_OFF_sensor управление датчиком включения выключения электричества </h1>
    <p class="text"><img src="{% static 'images/sensor.png' %}" alt=""></p>
    <p>сайт сенсора с описанием его API <a target="_blank"  href="https://tasmota.github.io/docs/" >Жми сюда</a></p>
    <h1 class="text" >Область применения разработанного программного обеспечения</h1>

    <p>Имеется база отдыха с множеством гостевых домов и комнат.</p>

<p>В каждой комнате имеется много потребителей электричества, таких как: свет верхний, торшер, утюг, чайник и т.д.
При заселении в дом отдыха, каждый гость регистрируется на сайте дома отдыха, администратор вносит локации, которые будут доступны гостю, для управления электроприборами.</p>
<p>Так же программа, может работать в частных домах, квартирах, офисах везде, где есть сеть WI-FI и приборы потребления электричества. </p>

      <p class="text"><img src="{% static 'images/House_page.jpg' %} " width="900" height="900" alt=""></p>











{% endblock %}
