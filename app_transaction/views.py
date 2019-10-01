from django.shortcuts import render
from django.db import transaction

from .models import Group

# Create your views here.

app_prefix = "transaction 3 -"

def save_with_exception(request):
    g1=Group()
    s_info = 'save with exception'
    g1.name='%s %s' % (app_prefix,s_info)
    g1.save()

    raise Exception("Error")
    # g1 is not stored to db

def save_without_exception(request):
    g1=Group()
    s_info = 'save without exception'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()
    # g1 is not stored to db

@transaction.non_atomic_requests # ignore atomic request for this view
def non_atomic(request):
    g1=Group()
    s_info = 'non atomic request'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    raise Exception("Error")
    # g1 is not stored to db

def save_outside():
    g1=Group()
    s_info = 'save outside'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

def outside(request):
    save_outside()
    raise Exception("Error")
    # g1 is not stored to db

def exception_in_try_except_block(request):
    try:
        g1=Group()
        s_info='exception in try except block'
        g1.name='%s %s' % ( app_prefix, s_info)
        g1.save()

        raise Exception("Error")
    except:
        pass

    #g1 is not stored to db

def outer_inner_1(request):
    g1=Group()
    s_info='outer transaction no exception 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic(): # context manager
            g2=Group()
            s_info='inner transaction with exception 1'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()
            raise Exception("Error") #this obj is not stored to db
    except:
        pass

    # g1, g2 is not stored to db

def outer_inner_2(request):
    g1=Group()
    s_info = 'outer transaction no exception 2'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic(): # context manager
            g2=Group()
            s_info = 'inner transaction with exception 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

        raise Exception("Error")
    except:
        pass

    #g1, g2 are not stored to db

def atomic_1(resquest):
    g1=Group()
    s_info = 'atomic_1 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_1 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_1 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    #g1, g2, g3 are not stored to db

def atomic_2(resquest):
    g1=Group()
    s_info = 'atomic_2 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_2 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_2 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    # g1, g2, g3 are not stored to db

def atomic_3(resquest):
    g1=Group()
    s_info = 'atomic_3 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_3 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_3 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    raise Exception("Error 2")

    # g1, g2, g3 are not stored to db

def atomic_4(resquest):
    g1=Group()
    s_info = 'atomic_4 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_4 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_4 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    raise Exception("Error 2")

    # g1, g2, g3 are not stored to db

def atomic_5(resquest):
    g1=Group()
    s_info = 'atomic_5 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_5 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

        raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_5 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    # g1, g2, g3 are not stored to db

@transaction.atomic
def atomic_6(resquest):
    g1=Group()
    s_info = 'atomic_6 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_6 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_6 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    # g1, g2, g3 are not stored to db

@transaction.atomic
def atomic_7(resquest):
    g1=Group()
    s_info = 'atomic_7 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_7 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_7 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    #g1, g2, g3 are not stored to db

@transaction.atomic
def atomic_8(resquest):
    g1=Group()
    s_info = 'atomic_8 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_8 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_8 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    raise Exception("Error 2")

    #g1, g2, g3 are not stored to db

@transaction.atomic
def atomic_9(resquest):
    g1=Group()
    s_info = 'atomic_9 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_9 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_9 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    auto_commit = transaction.get_autocommit()
    #transaction.set_autocommit(auto_commit) # raising an exception, it is forbidden when atomic block is active
    #transaction.rollback() # raising an exception, it is forbidden when atomic block is active
    print("function get_autocommit() : %s" % (auto_commit, ))

    sid = transaction.savepoint() # test
    print("save point id %s" % (sid, )) # test
    transaction.savepoint_rollback(sid)
    transaction.clean_savepoints()

    rollback_cond = transaction.get_rollback()
    print("rollback condition is %s" % (rollback_cond, ))
    transaction.set_rollback(rollback_cond)

    raise Exception("Error 2")

    #g1, g2, g3 are not stored to db
