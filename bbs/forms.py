#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django import forms
from bbs.models import Topic, Comment

class TopicForm(forms.ModelForm):
    title = forms.CharField(label=u'标题',required=False)
    content = forms.CharField(label=u'内容',required=False)
    
    def clean_title(self):
        title = self.cleaned_data.get("title").strip()
        if len(title) == 0:
            raise forms.ValidationError("请输入标题...")
        elif len(title) < 5:
            raise forms.ValidationError("标题太短哦...")
        elif len(title) > 100:
            raise forms.ValidationError("标题太长哦...")
        else:
            return title   

    def clean_content(self):
        content = self.cleaned_data.get("content").strip()
        if len(content) == 0:
            raise forms.ValidationError("请输入内容...")
        elif len(content) < 10:
            raise forms.ValidationError("正文内容太短哦...")
        elif len(content) > 2000:
            raise forms.ValidationError("正文内容太长哦...")
        else:
            return content   
                 
    class Meta:
        model = Topic
        fields = ('title','content')

  
class ReplyForm(forms.ModelForm):
    content = forms.CharField(max_length=1000,min_length=1,widget=forms.Textarea(attrs={'class':'form-control','rows':'5'})) 
    class Meta:
        model = Comment
        fields = ('content',)

class EditForm(forms.Form):
    content = forms.CharField(label=u'内容',max_length=1000,widget=forms.Textarea(attrs={'class':'form-control','rows':'20'}))   