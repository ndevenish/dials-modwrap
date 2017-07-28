project(cma_es)

add_library( cma_es INTERFACE )
target_include_directories(cma_es INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/..)

add_python_library ( cma_es_ext
            cma/cmaes.cpp
            cma_es_ext.cpp )
target_link_libraries(cma_es_ext scitbx)

