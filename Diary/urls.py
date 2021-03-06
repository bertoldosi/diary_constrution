from django.conf.urls import url
from django.urls import path
from Diary.views.construction.register_construction import Register_construction
from Diary.views.construction.show_construction_information import Show_construction_information
from Diary.views.construction.show_constructions import Show_constructions
from Diary.views.customer.edit_customer import Edit_customer
from Diary.views.customer.register_customer import Register_customer, autocompleteModel
from Diary.views.customer.show_customer import Show_customer
from Diary.views.diary.delete_contractor_equipment import Delete_contractor_equipment
from Diary.views.diary.delete_contractor_labor import Delete_contractor_labor
from Diary.views.diary.delete_diary import Delete_diary
from Diary.views.diary.delete_direct_labor import Delete_direct_labor
from Diary.views.diary.delete_equipment import Delete_equipment
from Diary.views.diary.delete_indirect_labor import Delete_indirect_labor
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
from Diary.views.enginner.enginner_register_customer import Enginner_register_customer
from Diary.views.enginner.register_engineer import Register_engineer
from Diary.views.enginner.show_customer import Show_engineer
from Diary.views.home.home_page import Index
from Diary.views.access.login import Login
from Diary.views.access.logout import Logout
from Diary.views.access.recover_password import Recover_Password
from Diary.views.user.access import Register_access
from Diary.views.user.customer_register_access import Customer_register_access
from Diary.views.user.delete_user import Delete_user

urlpatterns = [
    #Login
    path('home_page', Index, name='home_page'),
    path('', Login, name="login"),
    path('logout', Logout, name="logout"),
    #User
    path('register_access', Register_access, name="register_access"),
    path('recover_password', Recover_Password, name="recover_password"),
    path('customer_register_access', Customer_register_access, name="customer_register_access"),
    path('delete_user/<user_id>', Delete_user, name="delete_user"),
    #Customer
    path('register_customer', Register_customer, name="register_customer"),
    path('show_customer', Show_customer, name="show_customer"),
    path('edit_customer/<id_customer>', Edit_customer, name="edit_customer"),
    #Enginner
    path('register_engineer', Register_engineer, name="register_engineer"),
    path('show_engineer', Show_engineer, name="show_engineer"),
    path('edit_engineer', Edit_engineer, name="edit_engineer"),
    path('enginner_register_customer/<user>', Enginner_register_customer, name="enginner_register_customer"),
    #Construction
    path('register_construction', Register_construction, name="register_construction"),
    path('show_constructions', Show_constructions, name="show_constructions"),
    path('show_construction_information/<id_construction>', Show_construction_information, name="show_construction_information"),
    #Diary
    path('register_diary/<id_construction>', Register_diary, name="register_diary"),
    path('register_direct_labor/<diary>', Register_direct_labor, name="register_direct_labor"),
    path('register_indirect_labor/<diary>', Register_indirect_labor, name="register_indirect_labor"),
    path('register_equipment/<diary>', Register_equipment, name="register_equipment"),
    path('register_contractor_labor/<diary>', Register_contractor_labor, name="register_contractor_labor"),
    path('register_equipment_contractor/<diary>', Register_equipment_contractor, name="register_equipment_contractor"),
    path('register_climate/<diary>', Register_climate, name="register_climate"),
    path('register_observation/<diary>', Register_observation, name="register_observation"),

    path('delete_diary/<diary_id>', Delete_diary, name="delete_diary"),
    path('delete_direct_labor/<diary>/<direct_labor_id>', Delete_direct_labor, name="delete_direct_labor"),
    path('delete_indirect_labor/<diary>/<indirect_labor_id>', Delete_indirect_labor, name="delete_indirect_labor"),
    path('delete_contractor_labor/<diary>/<contractor_labor_id>', Delete_contractor_labor, name="delete_contractor_labor"),
    path('delete_equipment/<diary>/<equipment_id>', Delete_equipment, name="delete_equipment"),
    path('delete_equipment_contractor/<diary>/<equipment_contractor_id>', Delete_contractor_equipment, name="delete_equipment_contractor"),


    path('show_total_service/<diary>', Show_total_service, name="show_total_service"),
    path('show_diary', Show_diary, name="show_diary"),
    path('show_diary_information/<id_diary>', Show_diary_information, name="show_diary_information"),


    url(r'^ajax_calls/search/', autocompleteModel),
]