<?php
require ("Pessoa.php");
require ("Retangulo.php");
    class Fruta{
        //atributos
        public $nome;
        public $cor;

        //Métodos
        function __construct($nome, $cor){
            $this->nome = $nome;
            $this->cor = $cor;
        }
        function set_name($nome){
        $this->nome = $nome;
        }
        function get_name(){
            return $this->nome;
        }
        function set_color($cor){
            $this->cor = $cor;
            }
        function get_color(){
            return $this->cor;
        }
    }
    //criando um objeto
    $maca = new Fruta("Maçã_ifsp_turmaB ->", " Vermelha");
    $banana = new Fruta("Banana_ifsp_turmaB ->", " Amarela");

    /* $maca->set_name("maca_ifsp_turmaB");
    $banana->set_name("banana_ifsp_turmaB"); */

    echo $maca->get_name();
    echo $maca->get_color();
    echo "<br>" . "<br>" .$banana->get_name();
    echo $banana->get_color();

    $aluno1 = new Pessoa ("Luana", 17, "técnica em info");
    echo $aluno1->apresentar();

    $aluno2 = new Pessoa ("Poliana", 17, "técnica em info");
    echo $aluno2->apresentar();

    $retangulo = new Retangulo(2,4);
    echo "<br> Área do retângulo = ".$retangulo->calcular_area();
    echo "<br> Perímetro do retângulo = ".$retangulo->calcular_perimetro();
?>