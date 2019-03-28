"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e#&w7pcffq(jic1#99&ksc2t%aldc1dl$95-z(@kgz7&i!0xd1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mdeditor',
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 配置邮件服务

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtpdm.aliyun.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'mushan-blog@mail.mushan.top'
EMAIL_HOST_PASSWORD = 'ZB0320smtp'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/uploads')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

# mdeditor 富文本框配置

MDEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'height': 500,
        'toolbar': [
            'undo', 'redo', '|',
            'bold', 'del', 'italic', 'quote', 'ucwords', 'uppercase', 'lowercase', '|',
            # 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', '|',
            'list-ul', 'list-ol', 'hr', '|',
            'link', 'reference-link', 'image', 'code', 'code-block', 'table', 'datetime', '|',
            'html-entities', 'goto-line', 'help', '||', # 'info',
            'preview', 'watch', 'fullscreen',
        ],
        'upload_image_formats': ['jpg', 'jpeg', 'gif', 'png', 'bmp', 'webp'],   # 图片上传格式
        'image_folder': 'images',   # 图片保存文件夹名称
        'theme': 'default',         # 编辑框主题 dark / default
        'preview_theme': 'default',      # 预览区域主题 dark / default
        'editor_theme': 'default',       # edit 区域主题 pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,     # 是否开启查找替换功能
        'emoji': False,      # 是否开启表情功能
        'tex': True,        # 是否开启 tex 图表功能
        'flow_chart': True, # 是否开启流程图
        'sequence': True,   # 是否开启序列图
    }
}

# django-suit 配置

SUIT_CONFIG = {
    'ADMIN_NAME': '木杉后台管理',
    'HEADER_DATE_FORMAT': 'Y-m-d l',
    'HEADER_TIME_FORMAT': 'H:i',
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES ': True,
}