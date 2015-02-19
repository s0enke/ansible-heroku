# FIXME: clean up project structure, e.g. separate data from code
desc "Install virtualenv (a heresy!)"
task :venv => "venv/installed"

file "venv/installed" => "requirements.txt" do
  mkdir_p "venv"
  Dir.chdir("venv") do
    sh "curl -s -O https://pypi.python.org/packages/source/p/pip/pip-1.4.tar.gz"
    sh "curl -s -O https://pypi.python.org/packages/source/s/setuptools/setuptools-0.9.8.tar.gz"
    sh "curl -s -O https://raw.githubusercontent.com/pypa/virtualenv/1.9.1/virtualenv.py"
    sh "/usr/bin/env python virtualenv.py --no-site-packages ."
    sh "./bin/pip install -q -r ../requirements.txt"
    sh "touch installed"
  end
end
