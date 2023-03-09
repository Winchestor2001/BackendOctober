window.onload = () => {
    let loader = document.querySelector("#preloader");
    loader.style.opacity = 0;
    loader.style.visibility = "hidden";
};



let like = document.querySelector('.heart');
let title_text = document.querySelector('.title_text').text
like.addEventListener('click', (e) => {
    let prog_slug = e.target.dataset.favorit
    let like_classes = e.target.classList
    if (like_classes.contains('fa-regular') ) {
        like.classList.remove('fa-regular')
        like.classList.add('fa-solid')
        ajaxLike(prog_slug, true, title_text)
    } else {
        like.classList.remove('fa-solid')
        like.classList.add('fa-regular')
        ajaxLike(prog_slug, false, title_text)
    }
});

function ajaxLike(slug, is_liked, title){
    $.ajax({
        url: '/check_like/',
        type: "GET",
        data: { slug: slug, like: is_liked, title: title },
        success: function(data){
            console.log(data);
        }
    });
}