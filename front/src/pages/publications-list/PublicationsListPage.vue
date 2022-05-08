<template>
  
  <section class="publication-list">
    <PublicationItem  v-for=" publication in publication_list" :key="publication.id_pub" 
    :publication="publication"/>
  </section>
</template>

<script>
  // mejora: import { getPublications } from '@/services/api.js'
  import PublicationItem from "./PublicationItem.vue";
  import { getPublications } from "@/services/api.js";



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
        this.publication_list = await getPublications();
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
   /* flex-flow: row wrap; interesante para que vaje a
   la siguiente fila si no hay sitio*/
   flex-flow: row wrap; 


    margin: 0 auto;
    align-items: center;
    justify-content: space-evenly;


  }


</style>