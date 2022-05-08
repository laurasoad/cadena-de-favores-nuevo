<template>

<section>
  <h1>Nueva Publicación</h1>

  <form>
    
    <label for="title">Título:</label>
    <input type="text" key="title" v-model="pubInForm.title"/>

    <label for="description">Descripción:</label>
    
    <textarea id="description" v-model="pubInForm.description" placeholder="Agregue la descripción">
      Descripción textarea:</textarea>

    <label for="location">Lugar:</label>
    <input
      type="text"
      id="location"
      v-model="pubInForm.location"
    />
    
    <button @click.prevent="addNewPublication">Crear Publicación</button>
  </form>

</section>
  

</template>

<script>
import { v4 as uuidv4 } from "uuid";
import { addPublication } from "@/services/api.js";




export default {
    name: "NewPublicationSeekHelp",
    data() {
        return {

            pubInForm: {}
        }
    }, 
    methods: {

      isEmpty() {
      return (
        this.pubInForm.title == undefined ||
        this.pubInForm.description == undefined ||
        this.pubInForm.location == undefined
        );
      },

       async addNewPublication(){
         if(this.isEmpty()){
            alert("Rellene todos los campos, por favor");
         } else {
           //Guardamos los todos los datos de la publicación
            this.pubInForm.id_pub= uuidv4();
            this.pubInForm.publication_type ="0"
            //Se guarda el día
            let today = new Date()
            today = today.toISOString().slice(0,10)
            this.pubInForm.date = today

            //Imprime el objeto entero
            console.log(this.pubInForm)

            await addPublication(this.pubInForm);
            
        
          alert("La publicación se ha guardado correctamente")

          //Redirige a la lista de publicaciones
          this.$router.push(`/publications`);
        
         }

        





       }
    }

}
</script>

<style scoped>
section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1{
  /**
    color: #ab4493;  color bonito

  */
  font-size: 2em;  
  color: #ab4493;
}


form {  
  box-sizing: border-box;
  margin: 1em;
  border-radius: 0.5em;
  float: center;
  padding: 1em 1em 1em 1em;
  background-color: #fbfbfb; 
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}


input{
  background-color: #fbfbfb; 
  width: 75%; 
  min-width: 20em;

  height: 2.5em; 
  border: 1px solid #04AA6D;
  border-radius: 5px;  
  padding-left: 0.1em;
  margin-top: 0.2em;  
  margin-bottom: 0.8em; 
}


textarea{
  background-color: #fbfbfb; 
  width: 74%; 
  min-width: 20em;

  height: 150px; 
  border-radius: 5px;  
  border: 1px solid #04AA6D;
  margin-top: 0.2em;  
  margin-bottom: 0.8em; 
  
}


label{
  display: block; 
  float: center;  
}


button{
  height: 45px; 
  padding-left: 5px;
  padding-right: 5px;   
  margin-bottom: 20px; 
  margin-top: 10px;   
  text-transform: uppercase;
  background-color: #04AA6D; 
  border-color: #04AA6D; 
  border-style: solid; 
  border-radius: 10px;  
  width: 75%;   
  min-width: 20.2em;
  cursor: pointer;
  color:#fbfbfb
}


form input:focus{
  outline:0;
  border: 1px solid #97d848;
}


form textarea:focus{
  outline:0;
  border: 1px solid #97d848;
}







</style>