 // definindo o  tour!
 var tour = {
     id: "splarch-welcome",
     selectors: {
         init: '#architecture',
     },
     showCloseButton: true,
     i18n: {
        nextBtn: 'Proximo',
        prevBtn: 'Anterior',
        doneBtn: "Ok",
        skipBtn: "Sair",
        closeTooltip: "Fechar",
     },
     showCloseButton: true,
     showPrevButton: true,
     steps: [
         {
             title: "Architecture",
             content: "Module for architectures registration",
             target: "architecture",
             placement: "right",
             yOffset: 100,
             xOffset: -500,
             delay: 1,
             zindex: 0,
         },
         {
             title: "Auth",
             content: "Module of authentication and user control",
             target: "auth",
             placement: "right",
             yOffset: 40,
             xOffset: -500,
             delay: 1,
             zindex: 0
         },
         {
             title: "FAQ",
             content: "Check frequently asked questions about the software",
             target: "faq",
             placement: "right",
             xOffset: -500,
             yOffset: 30,
             zindex: 0
         },
         {
             title: "Requirement",
             content: "Module for Requirements registration",
             target: 'requirement',
             placement: "right",
             xOffset: -500,
             yOffset: 30,
             zindex: 0
         },
         {
             title: "Scoping",
             content: "Module for Scoping registration",
             target: 'scoping',
             placement: "right",
             xOffset: -500,
             yOffset: 40,
             zindex: 0
         },

         
     ]
 };

 // inicializa o tour
 hopscotch.startTour(tour);
 hopscotch.endTour();