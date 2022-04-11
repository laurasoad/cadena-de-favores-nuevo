<template>
  
  <section class="publication-list">
    <article class="pub-item" v-for=" publication in publication_list" :key="publication.id_pub">
      <p>Title: {{ publication.title }}</p>
      <p>Type: {{ publication.publication_type }}</p>
      <p> >> {{ publication.categories }}</p>
      <p>Location: {{ publication.location }}</p>
    
      <button>
         <router-link :to="`/publications/${publication.id_pub}`">Details</router-link>
      </button>
     
    </article>
  </section>
  <pre>{{publications}}</pre>
</template>

<script>
  //  import { getPublications } from '@/services/api.js'

  export default {
     
    name: 'PublicationList',
    data() {
      return {
        publication_list: [],
     
      }
    },

    mounted() {
   
      this.loadData()
    },

    methods: {
      async loadData() {
         
        //getPublications
        const response = await fetch('http://localhost:5000/api/publications')
        this.publication_list = await response.json()
        

      },
    }


  }
</script>

<style scoped>
  body {
    margin: 0 auto;
  }


  h1 {
    font-style: italic;
  }

  .publication-list {
    display: flex;
    margin: 0 auto;
    align-items: center;
    justify-content: space-between;

  }

  .pub-item {
    
    flex: 1 1 21rem;
    border: 2px solid #04AA6D;
    border-radius: 1em;
    margin: 1em 2em;
    padding: 1em 2em;
    /*max-width: 10em;*/
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    align-self: normal;


  }

  .pub-item:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}

  button {
  border: 2px solid #04AA6D;
  background-color: white;
  color: black;
  padding: 14px 28px;
  font-size: 16px;
  cursor: pointer;
  background-color: #04AA6D;
  color: white;
  
  text-shadow: 1px #837c7c;
  border-radius: 0.5em;
}

button:hover {
  color: #04AA6D;
  background-color: white;
  border-color: #04AA6D;

  
}

a:link, a:visited, a:active {
    text-decoration:none;
    color:#2c3e50
}
</style>