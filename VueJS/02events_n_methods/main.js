var app = new Vue({
    el: "#app",
    data: {
        lesson: "Events & Methods",
        counter: 0,
    },
    
    methods: {
        incrementCounter() {
            this.counter += 1
            console.log(this.counter)
            if (this.counter % 10 === 0) {
                alert("Counter is at "+ this.counter)
            }
        },
        overTheBox(){
            console.log('Over the box')
        }    
    },
})