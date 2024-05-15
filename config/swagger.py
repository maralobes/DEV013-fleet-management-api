class Endpoints:

    def taxi_route_swagger():{
"""
openapi: 3.0.3
info:
    title: Swagger Fleet Managment Api
    description: |-
        This endpoints is about request information about taxi, only id and plate.
paths:
    /taxis:
        get:
            summary: Returns taxis by page and limit
            description: Returns a 
            parameters:
              - name: query
                in: query
                type: string
                required: false
                description: Placa del taxi.
              - name: page
                in: query
                type: integer
                required: false
                description: Número de página de los resultados a recuperar. El valor predeterminado es 1.
              - name: limit
                in: query
                type: integer
                required: false
                description: Número de elementos por página. El valor predeterminado es 10.
            responses:
              '200':
              description: Un arreglo JSON de todos los taxis.
                schema:
                  type: array
                items:
                  type: object
                properties:
                  id:
                    type: integer
                    description: El ID del taxi.
                  plate:
                    type: string
                    description: Placa del taxi.
"""
    }
    
    def trajectories_route():{
        
    }
    
    def lasts_trajectories_route():{
        
    }