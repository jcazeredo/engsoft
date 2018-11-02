-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 02/11/2018 às 20:01
-- Versão do servidor: 10.1.35-MariaDB
-- Versão do PHP: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `engsoft`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cursos`
--

CREATE TABLE `cursos` (
  `id` int(11) UNSIGNED NOT NULL,
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `cursos`
--

INSERT INTO `cursos` (`id`, `nome`) VALUES
(3, 'Biologia'),
(4, 'Ciência da Computação'),
(1, 'Engenharia da Computação'),
(2, 'Física'),
(0, 'Nenhum');

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplinas`
--

CREATE TABLE `disciplinas` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(255) NOT NULL,
  `semestre` int(11) NOT NULL,
  `taxa_aprovacao` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `disciplinas`
--

INSERT INTO `disciplinas` (`id`, `nome`, `semestre`, `taxa_aprovacao`) VALUES
(1, 'Circuitos Elétricos I', 2, 0),
(2, 'Circuitos Elétricos II', 0, 0),
(3, 'Cálculo I', 0, 0),
(4, 'Física I', 0, 0),
(5, 'Probabilidade', 0, 0),
(6, 'Circuitos Elétricos I', 2, 0),
(7, 'Circuitos Elétricos II', 3, 0),
(8, 'Cálculo I', 4, 0),
(9, 'Física I', 5, 0),
(10, 'Probabilidade', 6, 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplinas_curso`
--

CREATE TABLE `disciplinas_curso` (
  `id` int(10) UNSIGNED NOT NULL,
  `curso_id` int(11) NOT NULL,
  `disciplina_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `disciplinas_curso`
--

INSERT INTO `disciplinas_curso` (`id`, `curso_id`, `disciplina_id`) VALUES
(2, 1, 3),
(3, 1, 1),
(4, 1, 2),
(5, 2, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `historico`
--

CREATE TABLE `historico` (
  `id` int(10) UNSIGNED NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `disciplina_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `historico`
--

INSERT INTO `historico` (`id`, `usuario_id`, `disciplina_id`) VALUES
(7, 8, 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `horarios_disciplinas`
--

CREATE TABLE `horarios_disciplinas` (
  `id` int(11) NOT NULL,
  `disciplina_id` int(11) NOT NULL,
  `segunda` int(11) NOT NULL,
  `terca` int(11) NOT NULL,
  `quarta` int(11) NOT NULL,
  `quinta` int(11) NOT NULL,
  `sexta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura para tabela `requisitos`
--

CREATE TABLE `requisitos` (
  `id` int(10) UNSIGNED NOT NULL,
  `disciplina_id` int(11) NOT NULL,
  `disciplina_requisto_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(10) UNSIGNED NOT NULL,
  `nome` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `privilegio` int(11) NOT NULL,
  `cartao_aluno` varchar(255) NOT NULL,
  `curso_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Fazendo dump de dados para tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome`, `senha`, `privilegio`, `cartao_aluno`, `curso_id`) VALUES
(2, 'ss', '1', 1, '2', 1),
(8, 'cristian dos anjos', '12', 1, '11', 2),
(9, 'dassd', 'dssd', 1, '123', 3),
(10, 'cu', 'adsasd', 1, '113', 3),
(12, 'nomed', 'senha', 1, '1234', 4),
(21, '14', '11', 0, '111', 0);

--
-- Índices de tabelas apagadas
--

--
-- Índices de tabela `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Único` (`nome`);

--
-- Índices de tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `disciplinas_curso`
--
ALTER TABLE `disciplinas_curso`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `historico`
--
ALTER TABLE `historico`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `requisitos`
--
ALTER TABLE `requisitos`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario` (`cartao_aluno`);

--
-- AUTO_INCREMENT de tabelas apagadas
--

--
-- AUTO_INCREMENT de tabela `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `disciplinas_curso`
--
ALTER TABLE `disciplinas_curso`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `historico`
--
ALTER TABLE `historico`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `requisitos`
--
ALTER TABLE `requisitos`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
