<template>
  <div class="addItemDiv">
    <h3>Add New Item To Store</h3>
      <!--Upload Image-->
    <form enctype="multipart/form-data">
      <div style="uploadImageTopDiv">
        <p class="uploadImageText">Upload item image</p>
        <p v-if="form.newItemImageName">{{form.newItemImageName}}</p>
      </div>
      <div v-if="!form.newItemImageName" class="dropbox">
        <input type="file" @change="onImageChange($event.target.files)"
          accept="image/*" class="fileInput">
        <p v-if="isSaving">
          Uploading file...
        </p>
        <p v-else>
          Drag your file(s) here to begin<br> or click to browse
        </p>
      </div>
    </form>
    <b-form-input class="adminInput" v-model="form.newItemName" placeholder="Enter item name"></b-form-input>
    <b-form-input class="adminInput" v-model="form.newItemPrice" type="number" placeholder="Enter item price"></b-form-input>
    <b-button class="adminButton" variant="light" @click="onReset">Reset</b-button>
    <b-button class="adminButton" variant="light" @click="onSubmit">Add Item</b-button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ItemForm',
  components: {

  },
  computed: {
    
  },
  data: function() {
    return {
      isInitial: true,
      isSaving: false,
      form: {
        newItemImageName: '',
        newItemImageFile: null,
        newItemName: '',
        newItemPrice: null,
      },      
    }
  },
  methods: {
    ...mapActions([
      'addItem'
    ]),
    onImageChange (file) {
      // TODO: Send this file to backend to process and store
      console.log('file', file)
      this.isSaving = true;
      this.form.newItemImageName = file[0].name;
      this.form.newItemImageFile = file[0]
      setTimeout(() => {this.isSaving = false;}, 1000) // To mimic saving
    },
    onReset () {
      this.form.newItemImageName = '';
      this.form.newItemImageFile = null;
      this.form.newItemName = '';
      this.form.newItemPrice = null;
    },
    async onSubmit () {
      await this.addItem(this.form);
      this.onReset();
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.addItemDiv {
  border: 1px solid grey;
  border-radius: 10px;
  padding: 1rem;
  margin: 0.5rem;
  background: var(--light-blue);
}

.adminInput {
  margin: 0.5rem 0;
}

.adminButton {
  margin: 0.5rem;
}

.uploadImageTopDiv {
  display: flex;
  justify-content: space-between;
}

.uploadImageText {
  text-align: left;
}

.dropbox {
  outline: 2px dashed grey; /* the dash box */
  outline-offset: -10px;
  background: rgb(224, 244, 255);
  color: dimgray;
  position: relative;
  cursor: pointer;
}

.fileInput {
  opacity: 0; /* invisible but it's there! */
  width: 100%;
  height: 100%;
  left: 0;
  position: absolute;
  cursor: pointer;
}

.dropbox:hover {
  background: lightblue; 
}

.dropbox p {
  text-align: center;
  padding: 1rem;
}
</style>
