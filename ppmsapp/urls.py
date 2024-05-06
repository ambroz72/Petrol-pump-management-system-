from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.home,name='home'),
    path('Eadmin/',views.Eadmin,name='Eadmin'),
    path('Euser/',views.Euser,name='Euser'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('signup/',views.signup,name='signup'),
    
    path('uprofile/',views.uprofile,name='uprofile'),
    path('add_report',views.add_report,name='add_report'),
    path('edit_report/<int:od>',views.edit_report,name='edit_report'),
    path('add_category',views.add_category,name='add_category'),
    
    path('edit_category/<int:od>',views.edit_category,name='edit_category'),
    path('showreport',views.showreport,name='showreport'),
    path('show_category',views.show_category,name='show_category'),
    path('show_user',views.show_user,name='show_user'),
    
    path('Login/',views.Login,name='Login'),
    path('Signup/',views.Signup,name='Signup'),
    path('Logout/',views.Logout,name='Logout'),
    path('eprofile/',views.eprofile,name='eprofile'),
    
    path('a_report',views.a_report,name='a_report'),
    path('e_report/<int:od>',views.e_report,name='e_report'),
    path('delete_cat/<int:od>',views.delete_cat,name='delete_cat'),
    path('deletecust/<int:od>',views.deletecust,name='deletecust'),
    path('delete_report/<int:od>',views.delete_report,name='delete_report'),
    path('a_category',views.a_category,name='a_category'),
    path('e_category/<int:od>',views.e_category,name='e_category'),
    
    path('tleave/',views.tleave,name='tleave'),
    path('aleave/',views.aleave,name='aleave'),
    path('show_leave/',views.show_leave,name='show_leave'),
    path('delete_leave/<int:od>',views.delete_leave,name='delete_leave'),
    
    path('register/',views.register,name='register'),
    path('show_register/',views.show_register,name='show_register'),
    path('accpts/<int:of>/<int:od>',views.accpts,name='accpts'),
    path('rejects/<int:of>/<int:od>',views.rejects,name='rejects'),
    path('tregister/',views.tregister,name='tregister'),
    path('delete_register/<int:od>',views.delete_register,name='delete_register'),
    
    path('new_passwd',views.new_passwd,name='new_passwd'),
    path('change_passwd',views.change_password,name='change_passwd'),
    path('accpt/<int:od>/<int:oa>',views.accpt,name='accpt'),
    path('rejctd/<int:od>/<int:oa>',views.rejctd,name='rejctd'),
    path('show_status/',views.show_status,name='show_status'),
    path('show_astatus/',views.show_astatus,name='show_astatus'),
    
    path('feed/',views.feed,name='feed'),
    path('show_feed/',views.show_feed,name='show_feed'),
    path('tfeed/',views.tfeed,name='tfeed'),
    path('delete_feed/<int:od>',views.delete_feed,name='delete_feed'),
    
    path('efeed/',views.efeed,name='efeed'),
    path('show_efeed/',views.show_efeed,name='show_efeed'),
    path('etfeed/',views.etfeed,name='etfeed'),
    path('delete_efeed/<int:od>',views.delete_efeed,name='delete_efeed'),
]
