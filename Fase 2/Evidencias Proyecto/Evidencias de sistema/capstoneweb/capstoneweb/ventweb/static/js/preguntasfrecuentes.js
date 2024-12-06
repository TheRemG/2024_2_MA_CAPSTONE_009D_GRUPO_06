
const faqQuestions = document.querySelectorAll('.faq-question');

faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
        const faqItem = question.closest('.faq-item');
        const answer = faqItem.querySelector('.faq-answer');
        faqItem.classList.toggle('active');

        if (faqItem.classList.contains('active')) {
            answer.style.display = 'block'; 
        } else {
            answer.style.display = 'none'; 
        }
    });
});
