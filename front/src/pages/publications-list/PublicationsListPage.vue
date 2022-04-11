<template>
  
  <section class="publication-list">
    <PublicationItem  v-for=" publication in publication_list" :key="publication.id_pub" 
    :publication="publication"/>
  </section>
</template>

<script>
  // mejora: import { getPublications } from '@/services/api.js'
  import PublicationItem from "./PublicationItem.vue";

  export default {
     
    name: 'PublicationList',
    components: {
      PublicationItem
    },
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
         
        //mejora: getPublications en services/api.js
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


</style>