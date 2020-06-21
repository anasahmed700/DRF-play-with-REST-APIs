var app = new Vue({
    el: '#app',
    
    data: {
        styleObject: {backgroundColor: 'green', border: "5px solid orange"},
        flag: true,
    },

    methods: {
        changeShape(){
            this.flag = !this.flag
        }
    },
})