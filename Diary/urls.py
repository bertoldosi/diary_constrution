from django.conf.urls import url
from django.urls import path
from Diary.views.construction.register_construction import Register_construction
from Diary.views.construction.select_customer import Select_customer
from Diary.views.construction.show_constructions import Show_constructions
from Diary.views.customer.edit_customer import Edit_customer
from Diary.views.customer.register_customer import Register_customer, autocompleteModel
from Diary.views.customer.show_customer import Show_customer
from Diary.views.diary.register_climate import Register_climate
from Diary.views.diary.register_contractor_equipment import Register_equipment_contractor
from Diary.views.diary.register_contractor_labor import Register_contractor_labor
from Diary.views.diary.register_diary import Register_diary
from Diary.views.diary.register_direct_labor import Register_direct_labor
from Diary.views.diary.register_equipment import Register_equipment
from Diary.views.diary.register_indirect_labor import Register_indirect_labor
from Diary.views.diary.register_observation import Register_observation
from Diary.views.diary.show_diary import Show_diary
from Diary.views.diary.show_diary_information import Show_diary_information
from Diary.views.diary.show_total_service import Show_total_service
from Diary.views.enginner.edit_customer import Edit_engineer
from Diary.views.enginner.register_engineer import Register_engineer
from Diary.views.enginner.show_customer import Show_engineer
from Diary.views.home.home_page import Index
from Diary.views.access.login import Login
from Diary.views.access.logout import Logout
from Diary.views.access.recover_password import Recover_Password
from Diary.views.user.access import Register_access

urlpatterns = [
    # Login
    path('home_page', Index, name='home_page'),
    path('', Login, name="login"),
    path('logout', Logout, name="logout"),
    # User
    path('register_access', Register_access, name="register_access"),
    path('recover_password', Recover_Password, name="recover_password"),
    # Customer
    path('register_customer', Register_customer, name="register_customer"),
    path('show_customer', Show_customer, name="show_customer"),
    path('edit_customer', Edit_customer, name="edit_customer"),
    # Enginner
    path('register_engineer', Register_engineer, name="register_engineer"),
    path('show_engineer', Show_engineer, name="show_engineer"),
    path('edit_engineer', Edit_engineer, name="edit_engineer"),
    # Construction
    path('register_construction', Register_construction, name="register_construction"),
    path('show_constructions', Show_constructions, name="show_constructions"),
    path('select_customer', Select_customer, name="select_customer"),
    # Diary
    path('register_diary', Register_diary, name="register_diary"),
    path('register_direct_labor', Register_direct_labor, name="register_direct_labor"),
    path('register_indirect_labor', Register_indirect_labor, name="register_indirect_labor"),
    path('register_equipment', Register_equipment, name="register_equipment"),
    path('register_contractor_labor', Register_contractor_labor, name="register_contractor_labor"),
    path('register_equipment_contractor', Register_equipment_contractor, name="register_equipment_contractor"),
    path('register_climate', Register_climate, name="register_climate"),
    path('register_observation', Register_observation, name="register_observation"),
    path('show_total_service', Show_total_service, name="show_total_service"),
    path('show_diary', Show_diary, name="show_diary"),
    path('show_diary_information', Show_diary_information, name="show_diary_information"),

    url(r'^ajax_calls/search/', autocompleteModel),
]
