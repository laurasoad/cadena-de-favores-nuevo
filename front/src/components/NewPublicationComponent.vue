


<template>

<section class="newpublication">
  <h1>Nueva Publicación</h1>

  <form>
    
    <label for="title">Título</label>
    <input type="text" key="title" v-model="pubInForm.title"/>

    <label for="description">Descripción</label>
    <textarea id="description" v-model="pubInForm.description" placeholder="Agregue la descripción">
    </textarea>

    <label for="location">Lugar</label>
    <input
      type="text"
      id="location"
      v-model="pubInForm.location"
    />
    
    Selecciona una categoría
    <select v-model="selectedCategory">
      <!-- 
        <option>Selecciona una categoría</option>
      -->
      <option v-for="category in categoriesList" :value="category" :key="category.id">
                {{ category.name}} 
      </option>
    </select>
    <div class="tagslist">
      <div v-for="(tag) in tagsList" :key="tag.tag_id" @click="onSelectingTags(tag.tag_id)" >
          {{ tag.name }}
      </div>
    <label for="inputtag">Etiquetas seleccionadas</label>
    <input type="text" key="inputtag" v-model="storagingSelectedTagsNames" disabled/>
    </div>
    <button @click.prevent="addNewPublication">Crear Publicación</button>
  </form>

</section>
  

</template>



<script>
import { v4 as uuidv4 } from "uuid";
import { addPublication } from "@/services/api.js";




export default {
    name: "NewPublicationComponent",
    data() {
        return {

            pubInForm: {},
            activeUser : JSON.parse(localStorage.getItem("activeUserWatcher")),
            categoriesList:[
              {"category_id":"CAT_GENERAL", "name":"General"}, 
              {"category_id":"CAT_EDUCATION", "name":"Educación"},
              {"category_id":"CAT_MUSIC", "name":"Música"},
              {"category_id":"CAT_HEALTH", "name":"Salud"}],
            selectedCategory: {},
            tagsList: [
              {"tag_id":1, "name":'#clases', isSelected: false},
              {"tag_id":2, "name":'#mates', isSelected: false },
              {"tag_id":3, "name": '#online' , isSelected: false},
              {"tag_id":4, "name": '#piano', isSelected: false}],
          
        }
    },
    props: {
        publication_type: {
            type: String,
            required: true
        }
    },
    emits: ["sendingNewUser"],
    computed: {
      isAnyUserActive() {
         console.log("i")
      console.log("isAnyUserActive ", this.activeUser != null)
      return this.activeUserId != null
  },
   storagingSelectedTags(){
     return this.tagsList.filter((element) => (element.isSelected == true)).map((element => element.tag_id))
   }
  ,
  storagingSelectedTagsNames(){
     return this.tagsList.filter((element) => (element.isSelected == true)).map((element => element.name))
   }
   },
  
    methods: {
      

      isEmpty() {
      return (
        this.pubInForm.title == undefined ||
        this.pubInForm.description == undefined ||
        this.pubInForm.location == undefined ||
        this.selectedCategory == {}//añadido
        );
      },

      async addNewPublication(){
         if(this.isEmpty()){
            alert("Rellene todos los campos, por favor");
         } else {
           //Guardamos los todos los datos de la publicación
            this.pubInForm.id_pub= uuidv4();
            this.pubInForm.publication_type = this.publication_type
            //Se guarda el día
            let today = new Date()
            today = today.toISOString().slice(0,10)
            this.pubInForm.date = today
            console.log(this.selectedCategory)
             this.pubInForm.category_id = this.selectedCategory["category_id"]
             this.pubInForm.tags = this.storagingSelectedTags

            //Imprime el objeto entero
            console.log(this.pubInForm)
            this.$emit("sendingNewPublication", this.pubInForm)         


            await addPublication(this.pubInForm);
            
        
          alert("La publicación se ha guardado correctamente")

          //Redirige a la lista de publicaciones
          this.$router.push(`/publications`);
        
         }
       },
        onSelectingTags(tag_identification) {
          console.log(tag_identification)
          this.tagsList[tag_identification-1]["isSelected"]= !this.tagsList[tag_identification-1]["isSelected"]      
         }

    }

}
</script>

<style scoped>

.newpublication {
  background-color: #fbfbfb; 
  border: 1px solid #fbfbfb;
  box-sizing: border-box;
  border-radius: 0.5em;
}

.tagslist {
padding: 20px 0px;
cursor: pointer;
}

/**
 1px solid #97d848; verde claro
 #04AA6D verde oscuro

 azul oscuro  #607d8b;
 azul claro #41b6e6;

*/
.tagslist div {
margin-right: 10px;
margin-bottom: 10px;
background: #41b6e6;
color: #ffffff;
display: inline-block;
padding: 7px 10px;
border-radius: 10px;
font-size: 13px;
}

.tagslist div:hover {
background: #607d8b;
}

section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1{
  /**
    color: #ab4493;  color bonito - morado

  */
  font-size: 2em;  
  color: #04AA6D;
}


form {  
  box-sizing: border-box;
  margin: 1em;
  float: center;
  padding: 1em 1em 1em 1em;
  background-color: #fbfbfb; 
  display: flex;
  flex-direction: column;
  align-items: center;
}


input{
  background-color: #fbfbfb; 
  width: 80%; 
  min-width: 20em;
  border: 1px solid #04AA6D;
  border-radius: 5px;  
  box-sizing:border-box;


  padding-left: 0.1em;
  height: 2.5em; 
  margin-top: 0.2em;  
  margin-bottom: 0.8em; 
}

select {
  background-color: #fbfbfb; 
  width: 90%; 
  height: 2.5em; 
  min-width: 20em;
  border: 1px solid #04AA6D;
  border-radius: 5px;  
  box-sizing:border-box;

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

form select:focus{
  outline:0;
  border: 1px solid #97d848;

}


form textarea:focus{
  outline:0;
  border: 1px solid #97d848;
}







</style>

