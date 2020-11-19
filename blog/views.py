from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Post
from .forms import CommentForm
# Create your views here

#-- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

#-- DetailView
class PostDV(DetailView, FormMixin):
    model = Post
    template_name = 'blog/post_detail.html'
    form_class = CommentForm

    # post 처리가 성공한 뒤 행할 행동
    def get_success_url(self):
        return reverse('blog:post_detail', args=(self.object.slug,)) # 디테일뷰 다시보여주기

    # template에 보낼 context 설정
    def get_context_data(self, **kwargs):
        context = super(PostDV, self).get_context_data(**kwargs)
        # context['form'] = CommentForm(initial= {
        #     'writer': '',
        #     'comment': ''                   # textfiled에 value값 설정
        # })
        context['comments'] = self.object.postcomment_set.all()
        return context

    # post 요청이 들어왔을 때
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()         # 현재 페이지 object get.
        form = self.get_form()                  # form 데이터 받아오기
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invaild(form)

    #  form_valid 함수
    def form_valid(self, form):
        comment = form.save(commit=False)       # form 데이터를 저장. 그러나 쿼리실행은 x
        comment.post = get_object_or_404(Post, pk=self.object.pk)   # post object를 call 하여 postcomment의 post로 설정(댓글이 속할 게시글 설정) pk로 pk - post id
        comment.save()                          # 수정된 내용대로 저장. 쿼리실행
        return super(PostDV, self).form_valid(form)