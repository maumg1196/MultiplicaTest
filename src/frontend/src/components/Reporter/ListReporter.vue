<template lang="html">
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
        <b-nav-item href="/events">Eventos</b-nav-item>
        <b-nav-item href="/reporters">Reporteros</b-nav-item>
        <b-nav-item href="/types">Tipos de Eventos</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <h2>Listado de Reporteros</h2>

          <div class="col-md-12">
            <div class="overflow-auto">
              <b-pagination
                v-model="currentPage"
                :total-rows="rows"
                :per-page="perPage"
                aria-controls="my-table"
              ></b-pagination>
            </div>
            <b-table 
              striped hover 
              :items="reporters"
              :fields="fields"
              :per-page="perPage"
              :current-page="currentPage">
              <template slot="number_events" slot-scope="data">
                {{data.item.number_events}}
              </template>
              <template slot="action" slot-scope="data">
                <b-button size="sm" variant="primary" :to="{ name:'Reporter', params: {reporterID: data.item.id} }">
                  Ver más
                </b-button>
              </template>
            </b-table>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      perPage: 5,
      currentPage: 1,
      fields: [
        { key: 'name', label: 'Nombre'},
        { key: 'number_events', label: 'Numero de Eventos'},
        { key: 'action', label: ''},
      ],
      reporters: [],
    }
  },
  methods: {
    getReporters () {
      const path = 'http://localhost:8000/reporters/'
      axios.get(path).then((response) => {
        this.reporters = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  computed: {
    rows() {
      return this.reporters.length
    }
  },

  created(){
    this.getReporters()
  }
}
</script>

<style lang="css" scoped>
</style>