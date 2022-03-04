# Using Rust Code on Odoo.sh

1. Create a rust package using `maturin` and a compatible python version (this
   project uses the `string_sum` example on python3.8.5. Odoo.sh currently uses
   3.8)
2. Build a wheel somehow using `maturin build` and add it into the Odoo addons
   repository (in this project, I used a submodule that contained the Odoo addon
   and the maturin package)
3. Add the maturin package to the Odoo repository `requirements.txt` using the
   `file:///home/odoo/src/user/...xxx-cp38-cp38-manylinux_2_24_x86_64.whl`
   syntax, indicating to install from absolute path.
4. As long as the Odoo.sh build can perform the
   `pip install -r requirements.txt`, the rust code is usable via python.
