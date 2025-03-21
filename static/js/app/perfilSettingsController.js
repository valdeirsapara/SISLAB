document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os links de navegação
    const categoryItems = document.querySelectorAll('.category-item');
    // Seleciona todas as seções de configuração
    const configSections = document.querySelectorAll('.config-section');
    
    // Função para mostrar uma seção específica e ocultar as outras
    function showSection(sectionId) {
        configSections.forEach(section => {
            section.style.display = (section.id === sectionId) ? 'block' : 'none';
        });
    }
    
    // Adiciona o evento de clique para cada item de navegação
    categoryItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove a classe 'active' de todos os itens
            categoryItems.forEach(nav => nav.classList.remove('active'));
            
            // Adiciona a classe 'active' ao item clicado
            this.classList.add('active');
            
            // Mostra a seção correspondente
            const sectionId = this.getAttribute('href').substring(1);
            showSection(sectionId);
        });
    });
    
    // Mostra a primeira seção por padrão
    if (categoryItems.length > 0) {
        categoryItems[0].classList.add('active');
        const firstSectionId = categoryItems[0].getAttribute('href').substring(1);
        showSection(firstSectionId);
    }
});
