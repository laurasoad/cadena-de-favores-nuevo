<template>
    <router-link to="/publications/add"><button>Nuevo contacto</button> </router-link>
  <section class="publication-list">
    <article class="publication-item" v-for="publication in publications" :key="publication.id_pub">
      <p>{{ publication.full_name }}</p>
      <p>{{ publication.phone }}</p>
      <p>{{ publication.email }}</p>
      <router-link :to="`/publications/${publication.id_pub}`">ver detalle</router-link>
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
        contacts: [],
     
      }
    },

    mounted() {
   
      this.loadData()
    },

    methods: {
      async loadData() {

        //getPublications


      
        
        

      },
    }


  }
</script>

<style scoped>
  h1 {
    font-style: italic;
  }

  .contact-item {
    border: 2px solid dodgerblue;
    border-radius: 1em;
    margin: 1em;
  }
</style>