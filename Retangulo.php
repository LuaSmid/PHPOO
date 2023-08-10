<?php
class Retangulo{
    //atributos
    public $altura;
    public $largura;

    //Métodos
    function __construct($altura, $largura)
    {
        $this->altura = $altura;
        $this->largura = $largura;        
    }
    function calcular_area(){
        return $this->largura * $this->altura;
    }
    function calcular_perimetro(){
        return $this->largura*2 + $this->altura *2;
    }
    function apresentar(){
        return  "<br>" .  "<br>" . "O perímetro do seu retangulo é  " . $this-> calcular_perimetro(). "<br>" . "A area do seu retangulo é " . $this-> calcular_area();
    }
}
?>