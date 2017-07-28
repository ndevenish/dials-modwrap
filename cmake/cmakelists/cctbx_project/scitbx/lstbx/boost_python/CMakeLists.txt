add_python_library ( scitbx_lstbx_normal_equations_ext
            lstbx_ext.cpp
            normal_equations.cpp )
target_link_libraries(scitbx_lstbx_normal_equations_ext scitbx_boost_python)

