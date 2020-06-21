var app = new Vue({
    el: '#app',
    data: {
        first_name: "Anas",
        last_name: "Ahmed",
    },
    // computed property is an extension of data model which store value in cache
    computed: {
      getRandomComputed() {
          return Math.random();
      },
      fullname(){
          return `${this.first_name} ${this.last_name}`;
      },
      reverseFullname(){
          first = this.first_name.split('').reverse().join('');
          last = this.last_name.split('').reverse().join('');
          return `${first} ${last}`;
      }
    },
    methods: {
        getRandomNumber(){
            return Math.random();
        }
    },
});