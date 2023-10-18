import axios from 'axios'

let baseUrl = '/api/vehicles/?format=json'

if (process.env.NODE_ENV === 'development') {
    baseUrl = 'http://localhost:8000/api/vehicles/?format=json'
}

const getAll = () => {
    return axios.get(baseUrl)
}

export default { getAll }